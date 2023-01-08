class Note:
    def __init__(self, new_name, new_surname, new_phone, new_birthday):
        if not all (isinstance(i, str) for i in [new_name, new_surname, new_phone, new_birthday]):
            raise TypeError('name, surname, phone and birthday must be str type.')
        self.__name = new_name
        self.__surname = new_surname
        self.__phone = new_phone
        self.__birthday = new_birthday

    @property
    def name(self):
        return self.__name
    
    @property
    def surname(self):
        return self.__surname

    @property
    def phone(self):
        return self.__phone
    
    @property
    def birthday(self):
        return self.__birthday

    def __str__(self):
        return f'{self.__name} {self.__surname} {self.__phone} {self.__birthday}'

class NoteBook:
    def __init__(self):
        self.__notebook = list()

    def show(self):
        print(*self.__notebook, sep = '\n')

    def __find(self, find_field):
        for note in self.__notebook:
            if find_field in [note.name, note.surname, note.phone, note.birthday]:
                return note
        raise ValueError("No such note in notebook.")

    def __add__(self, new_note):
        if not isinstance(new_note, Note):
            raise TypeError('note must be Note type.')
        if not all(note != new_note for note in self.__notebook):
            raise ValueError('Note already exists')
        self.__notebook.append(new_note)
        return self
    
    def __sub__(self, note):
        if (note in self.__notebook) :
            self.__notebook.remove(note)
            return self
        else:
            raise ValueError('No such note.')
    
    def __mul__(self, field):
        return self.__find(field)
