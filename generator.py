from difficulty import Difficulty
from question_store import QuestionStore
from spec import Spec
from subset_sum import subsetsum


class Generator(object):
    
    def __init__(self):
        self.easy = int(input("Enter the marks for easy questions > "))
        self.medium = int(input("Enter the marks for medium questions > "))
        self.hard = int(input("Enter the marks for hard questions > "))
        self.entry = Spec(self.easy, self.medium, self.hard)
        self.store = QuestionStore()
    
    def generate(self):
        easy_array = []
        medium_array = []
        hard_array = []
        
        easy_array = list(filter(lambda  x: x.difficulty == Difficulty.EASY, self.store.questions))
        easy_subset = subsetsum(easy_array, self.entry.easy)
        print(easy_subset)
        # for i in range(len(gen.questions)):
        #     if gen.questions[i].difficulty == Difficulty.EASY:
        #         easy_array.append(gen.questions[i]) 

        medium_array = list(filter(lambda x: x.difficulty == Difficulty.MEDIUM, self.store.questions))
        medium_subset = subsetsum(medium_array, self.entry.medium)
        print(medium_subset)
        # for i in range(len(gen.questions)):
        #     if gen.questions[i].difficulty == Difficulty.MEDIUM:
        #         medium_array.append(gen.questions[i]) 


        hard_array = list(filter(lambda x: x.difficulty == Difficulty.HARD, self.store.questions))
        hard_subset = subsetsum(hard_array, self.entry.hard)
        print(hard_subset)
        # for i in range(len(gen.questions)):
        #     if gen.questions[i].difficulty == Difficulty.HARD:
        #         hard_array.append(gen.questions[i]) 
        # hard_subset = subsetsum(hard_array, self.entry.hard)





        # for i in range(len(gen.questions)):
        #     for j in range(len(easy_subset)):
        #         if gen.questions[i].difficulty == Difficulty.EASY:
        #             if gen.questions[i].marks == easy_subset[j]:
        #                 question_list.append(gen.questions[i].id)

        # for i in range(len(gen.questions)):
        #     for j in range(len(medium_subset)):
        #         if gen.questions[i].difficulty == Difficulty.MEDIUM:
        #             if gen.questions[i].marks == medium_subset[j]:
        #                 question_list.append(gen.questions[i].id)

        # for i in range(len(gen.questions)):
        #     for j in range(len(hard_subset)):
        #         if gen.questions[i].difficulty == Difficulty.HARD:
        #             if gen.questions[i].marks == hard_subset[j]:
        #                 question_list.append(gen.questions[i].id)

        # print(question_list)


        


test = Generator()
test.generate()
