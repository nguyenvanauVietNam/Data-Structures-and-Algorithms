"""
Problem 7: Request Routing in a Web Server with a Trie
HTTPRouter using a Trie
For this exercise we are going to implement an HTTPRouter like you would find in a typical web server using the Trie data structure we learned previously.

There are many different implementations of HTTP Routers such as regular expressions or simple string matching, but the Trie is an excellent and very efficient data structure for this purpose.

The purpose of an HTTP Router is to take a URL path like "/", "/about", or "/blog/2019-01-15/my-awesome-blog-post" and figure out what content to return. In a dynamic web server, the content will often come from a block of code called a handler.

First we need to implement a slightly different Trie than the one we used for autocomplete. Instead of simple words the Trie will contain a part of the http path at each node, building from the root node /

In addition to a path though, we need to know which function will handle the http request. In a real router we would probably pass an instance of a class like Python's SimpleHTTPRequestHandler which would be responsible for handling requests to that path. For the sake of simplicity we will just use a string that we can print out to ensure we got the right handler

We could split the path into letters similar to how we did the autocomplete Trie, but this would result in a Trie with a very large number of nodes and lengthy traversals if we have a lot of pages on our site. A more sensible way to split things would be on the parts of the path that are separated by slashes ("/"). A Trie with a single path entry of: "/about/me" would look like:

(root, None) -> ("about", None) -> ("me", "About Me handler")

We can also simplify our RouteTrie a bit by excluding the suffixes method and the endOfWord property on RouteTrieNodes. We really just need to insert and find nodes, and if a RouteTrieNode is not a leaf node, it won't have a handler which is fine.
"""

class RouteTrie:
    def __init__(self, handler=""):
        self.root = RouteTrieNode()
        self.root.handler = handler

    def insert(self, path, handler):
        node = self.root
        parts = self.split_path(path)
        
        for part in parts:
            if part not in node.children:
                node.children[part] = RouteTrieNode()
            node = node.children[part]
        node.handler = handler

    def find(self, path):
        node = self.root
        parts = self.split_path(path)
        
        for part in parts:
            if part in node.children:
                node = node.children[part]
            else:
                return None
        return node.handler

    def split_path(self, path):
        if path == "/":
            return []
        return path.strip("/").split("/")


class RouteTrieNode:
    def __init__(self):
        self.children = {}
        self.handler = None


class Router:
    def __init__(self, root_handler, not_found_handler=None):
        self.route_trie = RouteTrie(root_handler)
        self.not_found_handler = not_found_handler

    def add_handler(self, path, handler):
        self.route_trie.insert(path, handler)

    def lookup(self, path):
        if not path:
            return self.route_trie.root.handler

        handler = self.route_trie.find(path)
        if handler is not None:
            return handler
        else:
            return self.not_found_handler

    def split_path(self, path):
        if path == "/":
            return []
        return path.strip("/").split("/")

# Testing the code with the provided test cases
router = Router("root handler", "not found handler")
router.add_handler("/home/about", "about handler")

print(router.lookup("/"))  # should print 'root handler'
print(router.lookup("/home"))  # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about"))  # should print 'about handler'
print(router.lookup("/home/about/"))  # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/me"))  # should print 'not found handler' or None if you did not implement one


# another test...
rout1 = Router("handle this", "")
rout1.add_handler("/something", "something handler")
rout1.add_handler("/something/somewhere", "somewhere handler")

# /home (not found)
print("\n/home (not found):", rout1.lookup("/home"))

# /something ('something handler')
print("/something ('something handler'):", rout1.lookup("/something/"))

# /something/somewhere ('somewhere handler'): somewhere handler
print("/something/somewhere ('somewhere handler'):",
      rout1.lookup("/something/somewhere"))
print()