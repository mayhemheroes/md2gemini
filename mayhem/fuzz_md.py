#!/usr/bin/env python3
import atheris
import sys


import fuzz_helpers

with atheris.instrument_imports():
    from md2gemini import md2gemini

ctr = 0
def TestOneInput(data):
    fdp = fuzz_helpers.EnhancedFuzzedDataProvider(data)
    global ctr
    ctr += 1
    try:
        md2gemini(fdp.ConsumeRandomString(), code_tag=fdp.ConsumeRandomString(), img_tag=fdp.ConsumeRandomString(), indent=fdp.ConsumeRandomString(),
              ascii_table=fdp.ConsumeBool(), frontmatter=fdp.ConsumeBool(), jekyll=fdp.ConsumeBool(),
              links=fdp.ConsumeRandomString(), plain=fdp.ConsumeBool(), strip_html=fdp.ConsumeBool(),
              base_url=fdp.ConsumeRandomString(), md_links=fdp.ConsumeBool(), link_func=fdp.ConsumeRandomString(),
              table_tag=fdp.ConsumeRandomString(), checklist=fdp.ConsumeBool())
    except IndexError:
        if ctr > 100:
            raise
        return -1

def main():
    atheris.Setup(sys.argv, TestOneInput)
    atheris.Fuzz()


if __name__ == "__main__":
    main()
