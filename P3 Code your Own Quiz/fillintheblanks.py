
easy_paragraph = '''The Olympic Games are a major international event which includes both "__1__" sports.The Paralympic Games for athletes with a "__2__".The Summer Olympic Games are held every "__3__" years.How many medals the olympics have"__4__"'''
medium_paragraph = '''The first Olympic Games were held in "__1__".The first modern games, held by the IOC, were hosted in "__2__".There are more than "__3__" athletes who compete in the Summer and Winter Olympics in __4__ different sports'''
hard_paragraph = '''The Paralympic Games were set up in "__1__"."__2__" organised a sporting event between different hospitals for rehabilitating soldiers."__3__"athletes competed in what was called the "__4__", which later became known as the first Paralympics.'''
blanks = ["___1___", "___2___", "___3___", "___4___"]

easy_answers = ['summer and winter','physical disability','four','4']
medium_answers = ['olympia','athens in 1896','13000','33']
hard_answers = ['1948','sir ludguttmanwig ','400','parallel olympics']

game_levels_list = ['easy', 'medium', 'hard']


# behavior: calls play_game function with the fill-in-the-blanks 
# string and answer set for a specified level
# input: (string) - input_level
# output: none
def start_game_with_choosen_level(input_level):
	if input_level == "easy":
		print "You've chosen the easy level!"
		print  easy_paragraph
		play_game(easy_paragraph, easy_answers)
	elif input_level == "medium":
		print "You've chosen the medium level!"
		print medium_paragraph
		play_game(medium_paragraph, medium_answers)
	elif input_level == "hard":
		print "You've chosen the hard level!"
		print hard_paragraph
		play_game(hard_paragraph , hard_answers)

#behavior:accepts the user input and answer key
#returns the true or false
#input:answer
#output:compares with answer 
def validate_user_input(index, answer_key):
	user_input = raw_input("What do you think: "+blanks[index]+" is : ")  
	return answer_key.lower() == user_input.lower() 	

#behvaior:this function invokes the user input makes sure it is not exceeded number of retired allowed
#input:number or tries
#output:decides the answers
#idx can also be understand as blanks_filled_in
def play_game(game_para, answers_array):
	retries_allowed = 3
	idx = 0
	while retries_allowed and idx < len(answers_array):
		if retries_allowed > 0 and validate_user_input(idx, answers_array[idx]):
			print replace_para_with_answers_filled(game_para, answers_array, idx)
			idx = idx + 1
			print  "That is correct! Congratulations!well done!"
		else:
			retries_allowed -= 1
			print "Please Try Again !You have : " + str(retries_allowed) + " strikes left!"

# returns the para with filled answers so far
def replace_para_with_answers_filled(game_para, answers_array, idx):
	while (idx >= 0):
		game_para = game_para = game_para.replace('"__' + str(idx+1) + '__"', answers_array[idx], 1)
		idx= idx-1
	return game_para


# This function starts the game.
def start_game():
	print "Hello! lets play fill in the blanks quiz"
	user_input_level = raw_input ('Choose your level: easy, medium, hard: ')
	if user_input_level in game_levels_list:
		start_game_with_choosen_level(user_input_level)
	else:
		print "############### Please choose a valid level ###############"
		start_game()


start_game()
