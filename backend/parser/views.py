from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status

from .models import ResumeUpload
from .serializers import ResumeUploadSerializer

import pdfplumber
import os
import stanza
from sentence_transformers import SentenceTransformer, util

# Download if not done
stanza.download('en')
nlp = stanza.Pipeline(lang='en', processors='tokenize,pos,lemma')
model = SentenceTransformer('all-MiniLM-L6-v2')

class ResumeParseView(APIView):
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request, *args, **kwargs):
        serializer = ResumeUploadSerializer(data=request.data)
        if serializer.is_valid():
            file_instance = serializer.save()
            file_path = file_instance.file.path  # Gets actual full path

            try:
                resume_text = self.extract_text(file_path)
                skills = self.extract_skills(resume_text)
                jd = request.data.get("job_desc", "")
                score = self.similarity_score(resume_text, jd)

                return Response({
                    "skills": skills,
                    "score": score
                }, status=status.HTTP_200_OK)

            except Exception as e:
                return Response({"error": str(e)}, status=500)
        return Response(serializer.errors, status=400)

    def extract_text(self, path):
        with pdfplumber.open(path) as pdf:
            return " ".join([p.extract_text() for p in pdf.pages if p.extract_text()])

    def extract_skills(self, text):
        doc = nlp(text)
        skills = set()
        for sentence in doc.sentences:
            for word in sentence.words:
                if word.upos in ['NOUN', 'PROPN'] and word.lemma:
                    skills.add(word.lemma.lower())
        return list(skills)

    def similarity_score(self, text1, text2):
        embeddings = model.encode([text1, text2])
        return round(util.cos_sim(embeddings[0], embeddings[1]).item() * 100, 2)
    


class ResumeParseBatchView(APIView):
    parser_classes = [MultiPartParser]

    def post(self, request, *args, **kwargs):
        files = request.FILES.getlist('files')
        jd = request.data.get("job_desc", "")

        if not files or not jd:
            return Response({"error": "Files and Job Description are required."}, status=400)

        response_data = []

        for file_obj in files:
            resume_instance = ResumeUpload.objects.create(file=file_obj)
            full_path = resume_instance.file.path
            resume_text = self.extract_text(full_path)
            skills = self.extract_skills(resume_text)
            score = self.similarity_score(resume_text, jd)
            response_data.append({
                "file_name": file_obj.name,
                "score": score,
                "skills": skills
            })

        return Response(response_data, status=200)

    def extract_text(self, path):
        with pdfplumber.open(path) as pdf:
            return " ".join([p.extract_text() for p in pdf.pages if p.extract_text()])

    def extract_skills(self, text):
        doc = nlp(text)
        skills = set()
        for sentence in doc.sentences:
            for word in sentence.words:
                if word.upos in ['NOUN', 'PROPN'] and word.lemma:
                    skills.add(word.lemma.lower())
        return list(skills)

    def similarity_score(self, text1, text2):
        embeddings = model.encode([text1, text2])
        return round(util.cos_sim(embeddings[0], embeddings[1]).item() * 100, 2)