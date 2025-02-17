import sys


def template(md_name):
    # file define
    file_name = md_name + ".md"
    md_title = "# " + md_name + "\n"
    md_path = "./" + file_name

    # read template
    with open("./DSA-Note-Template.md", 'r') as f:
        md_body = f.read()

    # write template
    with open(md_path, 'w') as f:
        f.write(md_title)
        f.write(md_body)

    print('generate file: ', md_path)


if __name__ == "__main__":

    # parser args.
    script_name = sys.argv[0]
    if len(sys.argv) > 1:
        file_name = sys.argv[1]
    else:
        file_name = "file_name"
    # generate markdown note.
    template(file_name)

