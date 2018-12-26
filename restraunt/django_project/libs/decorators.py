from django.http import HttpResponse
import json
from django.core.mail import mail_admins
from django.utils.translation import ugettext as _
import sys


def json_view(func):
    def wrap(request, *a, **kw):
        response = None
        try:
            response = func(request, *a, **kw)
            assert isinstance(response, dict)
        except KeyboardInterrupt:
            # Allow keyboard interrupts through for debugging.
            raise
        except Exception as e:
            # Mail the admins with the error
            exc_info = sys.exc_info()
            subject = 'JSON view error: %s' % request.path
            try:
                request_repr = repr(request)
            except Exception:
                request_repr = 'Request repr() unavailable'
            import traceback
            message = 'Traceback:\n%s\n\nRequest:\n%s' % (
                '\n'.join(traceback.format_exception(*exc_info)),
                request_repr,
            )
            mail_admins(subject, message, fail_silently=True)

            # Come what may, we're returning JSON.
            if hasattr(e, 'message'):
                msg = e.message
            else:
                msg = _('Internal error') + ': ' + str(e)
                response = {
                    'result': 'error',
                    'text': msg
                }

        res_json = json.dumps(response)
        return HttpResponse(res_json, content_type='application/json')
    return wrap
