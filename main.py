import argparse
from book_app.database import create_database, add_book, del_book, list_book


parser = argparse.ArgumentParser(description="Book manager")

subparsers = parser.add_subparsers(title="Subcommands", dest="subcommand")

# Subcommand to create a database
database_parser = subparsers.add_parser("database", help="Create database")

# Subcommand to add a book
add_parser = subparsers.add_parser("add", help="Add a new book")
add_parser.add_argument("name_of_the_book", type=str, help="Book to be add")
add_parser.add_argument("author", type=str, help="Book author")

# Subcommand to del a book
del_parser = subparsers.add_parser("del", help="Delete a book")
del_parser.add_argument("title", type=str, help="Book to be delete")

# Subcommand to list the books
list_parser = subparsers.add_parser("list", help="List books")

args = parser.parse_args()

if __name__ == '__main__':
    if args.subcommand == "database":
        create_database()
    elif args.subcommand == "add":
        add_book(args.name_of_the_book, args.author)
    elif args.subcommand == "del":
        del_book(args.title)
    elif args.subcommand == "list":
        list_book()
