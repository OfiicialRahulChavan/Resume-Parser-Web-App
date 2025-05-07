from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser,FormParser
from .utils import extract_text_from_pdf, extract_skills_spacy, compute_similarity


class SingleResumeParser(APIView):
    parser_classes = [MultiPartParser, FormParser]
    def post(self, request):
        file = request.FILES['file']
        job_desc = request.data['job_desc']
        resume_text = extract_text_from_pdf(file)
        resume_skills = extract_skills_spacy(resume_text)
        jd_skills = extract_skills_spacy(job_desc)
        matched_skills = list(set(resume_skills) & set(jd_skills))
        score = compute_similarity(resume_text, job_desc)

        return Response({
            "file_name": file.name,
            "resume_skills": resume_skills,
            "jd_skills": jd_skills,
            "matched_skills": matched_skills,
            "score": score
        })


class BatchResumeParser(APIView):
    parser_classes = [MultiPartParser, FormParser]
    def post(self, request):
        files = request.FILES.getlist('files')
        job_desc = request.data['job_desc']
        results = []

        for file in files:
            resume_text = extract_text_from_pdf(file)
            resume_skills = extract_skills_spacy(resume_text)
            jd_skills = extract_skills_spacy(job_desc)
            matched_skills = list(set(resume_skills) & set(jd_skills))
            score = compute_similarity(resume_text, job_desc)

            results.append({
                "file_name": file.name,
                "resume_skills": resume_skills,
                "jd_skills": jd_skills,
                "matched_skills": matched_skills,
                "score": score
            })

        return Response(results)