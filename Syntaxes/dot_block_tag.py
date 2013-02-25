import re
from timeit import timeit


def collapse_re(exp):
    exp = exp.splitlines()
    exp = [re.sub(r'\s+#\s+.*$', '', i) for i in exp]  # strip comments
    exp = ''.join(exp)
    exp = exp.replace(' ', '')
    return exp

tag_id = r'(#[\w-]+)'

tag_class = r'(\.[\w-]+)'

tag_name = r'''(
  ([#!]\{[^}]*\}) # interpolated name
  | # or
  (\w(([\w:-]+[\w-])|([\w-]*))) # regular name
)'''

# unless they are inside strings, we dont support parens inside
# attrs, since it's impossible to detect if they are balanced
tag_attrs = r'(\(([^()\'\"]*((\'([^\']|((?<!\\)\\\'))*\')|(\"([^\"]|((?<!\\)\\\"))*\")))*[^()]*\))*'

tag = r'''
( # a jade tag starts with
  ( # a pure tag (name/id/classes)
    ( # starting with id or class
      %(tag_id)s
      | # or
      %(tag_class)s
    )
    | # or
    %(tag_name)s # a tag name
  )
  ( # followed by an optional number of
    %(tag_id)s
    | # or
    %(tag_class)s
    | # or
    %(tag_attrs)s
  )*
)''' % {'tag_id': tag_id, 'tag_class': tag_class, 'tag_name': tag_name, 'tag_attrs': tag_attrs}

dot_block_tag = r'''
(?=[\w.#].*?\.$) # first, let's see if it meets the most basic requirements
(?=( # a dot text block tag
  ((:\s+)?%(tag)s)+ # is a tag followed by any number of subtags
)\.$) # and ending the line with a '.'
''' % {'tag': tag}

dot_block_tag = collapse_re(dot_block_tag)

if __name__ == '__main__':
    r = re.compile(dot_block_tag)
    for i in [
      ': asdfsdf.',
      '.',
      'atag',
      'atag.cls.cls#id',
      '.cls: atag.cls: #idtag',
      '.cls lorem ipsun.',
      '.cls= lorem ipsun.',
      'atag(attr, attr2=(1+1), attr3=3).',
      'atag(attr, attr2=(1+1), attr3=3)(more="attrs"): withsub: .cls(abc=1).',
      'atag(attr, att="("): asdf r2= abc, attr3="test"().',
      'atag(attr, att="("): asdf (r2= abc, attr3="test").',
      'atag(attr, attr2=abc, attr3="te(s"dfsd)st").',
      '#{null+123}}.',
      'atag:  :  asdfdsf.',
      'atag.cls.cls#id.',
      '.cls: atag.cls: #idtag.',
      'atag(attr, attr2=abc, attr3="te(sdfsd)st").',
      'atag(attr, attr2=abc, attr3="te(s\\"dfsd)st").',
      "atag(attr, attr2=abc, attr3='te(s\\'dfsd)st', asdfasdf=')', asdf=\"asdf))\").",
      'atag(attr, attr2=2)(more="attrs"): withsub: .cls(abc=1).',
      'div.class.another: p.red(style="").asdfsd(lol=123)#ohno.',
      '#{null+123{}.',
      'abc(123)asd.'  # oddly this should match, despite an unexpected output
    ]:
        print '"%s": %s' % (i, r.match(i))

    print dot_block_tag.replace('\\', '\\\\').replace('"', '\\"')
