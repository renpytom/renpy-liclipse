#!/usr/bin/env python
from __future__ import print_function

import argparse
import os

import keywords

ROOT = os.path.dirname(os.path.abspath(__file__))

def quote(s):
    return "'" + s + "'"

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dist", "-d", action="store_true", help="Output the result to the dist directory.")
    ap.add_argument("--output", "-o", help="The file to output the result to.")
    ap.add_argument("--liclipse", "-l", help="The path a Liclipe or Eclipse we will install our output to.")

    args = ap.parse_args()


    # Determine the output file name.
    output = args.output

    if args.dist:
        output = os.path.join(os.path.dirname(ROOT), "dist", "renpy.liclipse")

    if output is None and args.liclipse:
        plugins = os.path.join(args.liclipse, "plugins")

        editor = None

        for dn in sorted(os.listdir(plugins)):
            if dn.startswith("com.brainwy.liclipse.editor_"):
                editor = dn

        if editor is None:
            raise Exception("com.brainwy.liclipse.editor plugin not found.")

        languages = os.path.join(plugins, editor, "languages")

        if not os.path.isdir(languages):
            raise Exception("Couldn't find languages directory.")

        output = os.path.join(languages, "renpy.liclipse")

    if output is None:
        ap.error("Please give one of the --dist, --output, or --liclipse arguments.")


    # Read in the template file.
    with open(os.path.join(ROOT, "renpy.tmpl.liclipse"), "r") as f:
        data = f.read()

    data = data.replace("KEYWORDS", ",".join(quote(s) for s in keywords.keywords))
    data = data.replace("PROPERTIES", ",".join(quote(s) for s in keywords.properties))

    # Write the output file.
    print("Writing", output)

    with open(output, "w") as f:
        f.write(data)


if __name__ == "__main__":
    main()
