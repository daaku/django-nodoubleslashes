from django.http import HttpResponseRedirect
import re

multislash_re = re.compile('/{2,}')

class NoDoubleSlashes:
    """
    Some poorly configured redirecting sites (like 123-reg) add extra slashes to
    URLs when they are redirected, e.g. example.com/blah redirects to
    example.net//blah . This middleware eliminates any multiple slashes from
    incoming request paths.
    """
    def process_request(self, request):
        if '//' in request.path:
            new_path = multislash_re.sub('/', request.path)
            return HttpResponseRedirect(new_path)
        else:
            return None
