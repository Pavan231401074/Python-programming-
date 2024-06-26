def categorize_books_sorted():

    books = {}

    

    while True:

        try:

            user_input = input().strip()

        except EOFError:

            break

        

        if not user_input:

            break

        

        title, genre = user_input.split(',')

        genre = genre.strip()

        

        if genre in books:

            books[genre].append(title)

        else:

            books[genre] = [title]

    

    for genre in sorted(books.keys()):

        print(f"{genre}: {', '.join(books[genre])}")



categorize_books_sorted()
