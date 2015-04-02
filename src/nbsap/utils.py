import re

DENIED_TAGS = ('html', 'head', 'link', 'body', 'meta', 'script', 'title',
               'style', 'applet',)
RE_CODE = re.compile('(\d+\.)*\d+$')
RE_DIGIT_CODE = re.compile('\d+$')
RE_ACTION_CODE = re.compile('[^\d]*(\d+)([a-zA-Z]*)$')


def remove_tags(html, tags=DENIED_TAGS):
    """ Returns the given HTML with given tags removed. """
    tags_re = '(%s)' % '|'.join(re.escape(tag) for tag in tags)
    starttag_re = re.compile(r'<%s(/?>|(\s+[^>]*>))' % tags_re, re.U)
    endtag_re = re.compile('</%s>' % tags_re)
    html = starttag_re.sub('', html)
    html = endtag_re.sub('', html)
    return html
