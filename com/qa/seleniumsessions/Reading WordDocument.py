import docx


def ReadingTextDocuments(fileName):
    doc = docx.Document(fileName)

    completedText = []

    for paragraph in doc.paragraphs:
        completedText.append(paragraph.text)

    return '\n' .join(completedText)


print(ReadingTextDocuments("‪C:\\Users\\Nxt\\PycharmProjects\\PythonSeleniumsessions\\PDF file\\ATM  Requirements.docx"))
