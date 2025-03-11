import os
import jinja2
import json
import argparse

if __name__ == "__main__":
    # Default files
    payload_file = "payload.json"
    external_links_file = "links.json"

    parser = argparse.ArgumentParser()
    parser.add_argument('--empty', default=False, action='store_true')
    parser.add_argument('--template', default="index.html.j2")

    args = parser.parse_args()

    with open(payload_file) as fin:
        payload = json.load(fin)

    with open(external_links_file) as fin:
        links = json.load(fin)

    template_folder = os.path.dirname(args.template)
    environment = jinja2.Environment(loader=jinja2.FileSystemLoader(template_folder))
    template = environment.get_template(os.path.basename(args.template))


    if args.empty:
        print(template.render())
    else:
        print(template.render(results=payload, links=links, variant="ENST00000375549.8:c.100del"))
