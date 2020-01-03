class Looking:
    def __enter__(self):
        import sys
        self.original = sys.stdout.write
        sys.stdout.write = self.reverse_write
        return "ABCDAEFG"
    
    def reverse_write(self, text):
        self.original(text[::-1])
    
    def __exit__(self, exc_type, exc_value, traceback):
        import sys
        sys.stdout.write = self.reverse_write
        if exc_type is ZeroDivisionError:
            print("by zero")
            return True
        
    
with Looking() as what:
    print("hello")
    print(what)
