"""
Author: Alejandro Sanchez Uribe
Date: 19 Dec 2019
"""


# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self):
        # Initialize the node with children as before, plus a handler
        self.children = {}
        self.handler = None


# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode()
        self.handler = None

    def insert(self, path, handler):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path

        current_node = self.root

        for part in path:
            if part not in current_node.children:
                current_node.children[part] = RouteTrieNode()
            current_node = current_node.children[part]

        current_node.handler = handler

    def find(self, path):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        current_node = self.root

        for part in path:
            if part not in current_node.children:
                return None
            current_node = current_node.children[part]

        return current_node.handler


class Router:
    def __init__(self, handler, not_found_handler):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.trie = RouteTrie()
        self.handler = handler
        self.not_found_handler = not_found_handler

    def split_path(self, str_path):
        # you need to split the path into parts for
        # both the add_handler and lookup functions,
        # so it should be placed in a function here
        str_path = str_path.strip('/')
        path = str_path.split('/')
        return path

    def add_handler(self, str_path, handler):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        if str_path == '/':
            self.handler = handler
            return

        path = self.split_path(str_path)
        self.trie.insert(path, handler)

    def lookup(self, str_path):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        if str_path == '/':
            return self.handler

        path = self.split_path(str_path)
        output = self.trie.find(path)

        if output is None:
            return self.not_found_handler + str_path
        else:
            return output


# Test Cases below:

# create the router and add a route
router = Router('root handler', '404 page not found: /...')
router.add_handler('/home/about', 'about handler')
# add a route

print(router.lookup('/'))
# should print 'root handler'

print(router.lookup('/home'))
# should print 'not found handler'

print(router.lookup('/home/about'))
# should print 'about handler'

print(router.lookup('/home/about/'))
# should print 'about handler'

print(router.lookup('/home/about/me'))
# should print 'not found handler'

print(router.lookup('//'))
# should print 'not found handler'

router.add_handler('/home/about/', 'about handler 2')
print(router.lookup('/home/about'))
# should print 'about handler 2' since it should just modify about even with the '/' at the end

router.add_handler('//', 'slash handler')
print(router.lookup('//'))
# should print 'slash handler'

router.add_handler('/', 'new root handler')
print(router.lookup('/'))
# should print 'new root handler' since it replaces the original handler

router.add_handler('/////////////////////////////////////////////', 'deep handler')
print(router.lookup('/////////////////////////////////////////////'))
# should print 'deep handler'
