import sys
import os
import shutil
import re
from string import Template

MASTER = Template(
r"""\input{../../common/common.tex}

\title{$course_name}

\begin{document}

\maketitle
\tableofcontents

\input{$chapter}

\bibliographystyle{plainnat}
\bibliography{../../common/bibliography}
\end{document}

%%% Local Variables:
%%% TeX-master: t
%%% End:
""")

BASE = "/Users/tulloch/Mathematics/Cambridge"


def main():
    course_name, chapter_name = sys.argv[1:]
    course_dir = BASE + "/" + course_name + "/LectureNotes"
    os.makedirs(course_dir)

    pretty_course_name = re.sub(r"(\w)([A-Z])", r"\1 \2", course_name)

    with open(course_dir + "/" + "master.tex", "w+") as f:
        f.write(MASTER.substitute(
            chapter=chapter_name + ".tex",
            course_name=pretty_course_name))

    with open(course_dir + "/" + chapter_name + ".tex", "w+") as f:
        f.write("\n")

    with open(course_dir + "/" + "Makefile", "w+") as f:
        f.write("include ../../common/Makefile")

if __name__ == "__main__":
    main()
