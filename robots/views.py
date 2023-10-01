from django.http import FileResponse
from .services.make_statistics_service import MakeReportService


def download_report(request):
    report = MakeReportService().make_report()
    response = FileResponse(open(report, 'rb'))
    return response

