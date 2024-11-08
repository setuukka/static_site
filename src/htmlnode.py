class HtmlNode(tag: str = None, value: str = None, children: list = None, props: dict = None):
    def __init__(self, tag, value, children, props):
        self.tag = tag
        self. value = value
        self.children = children
        self.props = props


    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        for key, value in self.props.items():
            return f" {key} {value}"

    def __repr__(self):
        return f"HtmlNode - tag: {tag}, value: {value}, children: {children}, props: {props}"