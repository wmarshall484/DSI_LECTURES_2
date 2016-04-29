from library import Library

anza = Library(['Grapes of Wrath', 'Pinocchio', '1984'])
anza.add_book('Winnie the Poo')
print 'All books:', anza.all_books()

print 'Holder is', anza.book_holder('Winnie the Poo')

anza.checkout('Winnie the Poo', 'Ryan')
print 'Holder is', anza.book_holder('Winnie the Poo')

anza.checkin('Winnie the Poo')
print 'Holder is', anza.book_holder('Winnie the Poo')
