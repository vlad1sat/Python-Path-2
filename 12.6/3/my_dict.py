class MyDict(dict):

    def get(self, key):
        if key in self:
            return self[key]
        return 0


new_dict = MyDict()
new_dict['a'] = 1
new_dict['b'] = 2
print(new_dict)
print(new_dict.get('c'))
