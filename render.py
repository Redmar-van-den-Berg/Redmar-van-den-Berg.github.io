import jinja2
import json


if __name__ == "__main__":
    template_file = "index.html.j2"
    payload_file = "payload.json"
    external_links_file = "links.json"

    with open(payload_file) as fin:
        payload = json.load(fin)

    with open(external_links_file) as fin:
        links = json.load(fin)

    environment = jinja2.Environment(loader=jinja2.FileSystemLoader("."))
    template = environment.get_template(template_file)

    print(template.render(results=payload, links=links, variant="ENST00000375549.8:c.100del"))

