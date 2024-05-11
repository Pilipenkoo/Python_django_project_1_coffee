from abc import abstractclassmethod, ABC

class Piece(ABC):
    @abstractclassmethod
    def move(self):
        pass
    
class Queen(Piece):
    def move(self):
        print('Ход')
        
a = Piece()
b =   Queen(
)

a.move()
b.move()