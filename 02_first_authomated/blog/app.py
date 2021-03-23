from blog import Blog

MENU_PROMT = 'Enter "c" to create a blog, "l" to list blogs, "r" to read one, "p" to create a post, or "q" to quit:'
POST_TEMPLATE = """
--- {} ---

{}

"""

blogs = dict()  # create a new dictionary blog_name : Blog object

def menu():
    # Show the user the available blogs
    # Let the user make a choice
    # Do something with that choice
    # Eventually exit
    print_blogs()
    selection = input(MENU_PROMT)
    while selection != 'q':
        if selection == 'c':
            ask_create_blog()
        elif selection == 'l':
            print_blogs()
        elif selection == 'r':
            ask_read_blog()
        elif selection == 'p':
            ask_create_post
        selection = input(MENU_PROMT)

def print_blogs():
    ## Print the available blogs
    #print("Blogs!")
    for key, blog in blogs.items(): # [(blog_name, Blog), (blog_name, Blog)]
        print('- {}'.format(blog))

def ask_create_blog():
    title = input('Enter your blog title: ')
    author = input('Enter your name: ')

    blogs[title] = Blog(title, author)

def ask_read_blog():
    title = input('Enter the blog title you want to read: ')

    print_posts(blogs[title])

def print_posts(blog):
    for post in blog.posts:
        print_post(post)

def print_post(post):
    print(POST_TEMPLATE.format(post.title, post.content))

def ask_create_post():
    blog = input("Enter the blog title you want to create a post in: ")
    title = input("Enter your post title: ")
    content = input("Enter your post content: ")

    blogs[blog].create_post(title, content)

