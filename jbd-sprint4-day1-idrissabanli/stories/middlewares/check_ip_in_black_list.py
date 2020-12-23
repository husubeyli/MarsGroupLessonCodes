from django.utils.deprecation import MiddlewareMixin
from django.core.exceptions import PermissionDenied
from django.conf import  settings
from django.utils.timezone import now
import os


class CheckIPInBlackList(MiddlewareMixin):
    IP_BLACK_LIST = [
        '127.0.0.2'
    ]

    def process_view(self, request, *args, **kwargs):
        ip = request.META['REMOTE_ADDR']
        if ip in self.IP_BLACK_LIST:
            raise PermissionDenied()


class LoggingRequest(MiddlewareMixin):
    def write_to_file_logs(self, message, event, time,):
        file_name = os.path.join(settings.BASE_DIR, 'debug.log')
        with open(file_name, 'a') as f:
            f.writelines(f'{message}, {time}, {event} \n')

    def process_exception(self, request, *args, **kwargs):
        path = request.build_absolute_uri()
        self.write_to_file_logs(path, now(), 'error')

    def process_view(self, request, *args, **kwargs):
        path = request.build_absolute_uri()
        self.write_to_file_logs(path, now(), 'success')
