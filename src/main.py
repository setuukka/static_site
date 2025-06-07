#./main.sh
# hello world

from textnode import TextNode, TextType

def main():
    dummy_text_node = TextNode("This is some text", TextType.LINK, "https://google.com")
    print(dummy_text_node)


main()