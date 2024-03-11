class Grade:
    def c(self,gr):
        if (gr >= 90):
            return "Grade A"
        elif (gr >= 80):
            return "Grade B"
        elif (gr >= 70):
            return "Grade C"
        else:
            return "Fail"
# obj=Grade()
# gr=float(input("Enter your score : "))
# obj.c(gr)