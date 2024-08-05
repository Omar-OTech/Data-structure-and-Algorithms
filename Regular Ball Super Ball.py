class Ball(object):
    def __init__ (self, ball_type = 'regular'):
        self.ball_type = ball_type


print(Ball().ball_type)            # "regular"
print(Ball('super').ball_type)     # "super"