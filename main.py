from presenter import * #What does this do?

# Main method to process a full-page sheet
# Submits three times, because there are three matches on one sheet
def main(presenter):
	for s in (0,16,32): #What the heck does this mean?
	  presenter.shiftDown(s)

		# The numberings of the fields are important; you reference them by number in server.py
		bkks = presenter.rangefield('N-11', 0, 4) #Barbara Katz Knowledge Subject
		presenter.set("BK Knowledge of Subject", bkks) #0
		
		bkop = presenter.rangefield('N-12', 0, 4) #Barbara Katz Organized in Presenting
		presenter.set("BK Organized in Presenting", bkop) #1
		
		bkcd = presenter.rangefield('N-13', 0, 4) #Barbara Katz Effective in Content Delivery
		presenter.set("BK Effective in Content Delivery", bkcd) #2
		
		bktm = presenter.rangefield('N-14', 0, 4) #Barbara Katz Teaching Methods Used Effectively
		presenter.set("BK Teaching Methods Used Effectively", bktm) #3
		
		pmks = presenter.rangefield('AD-11', 0, 4) #Pamela D. Miller Knowledge Subject
		presenter.set("PM Knowledge of Subject", pmks) #4
		
		pmop = presenter.rangefield('AD-12', 0, 4) #Pamela D. Miller Organized in Presenting
		presenter.set("PM Organized in Presenting", pmop) #5
		
		pmcd = presenter.rangefield('AD-13', 0, 4) #Pamela D. Miller Effective in Content Delivery
		presenter.set("PM Effective in Content Delivery", pmcd) #6
		
		pmtm = presenter.rangefield('AD-14', 0, 4) #Pamela D. Miller Teaching Methods Used Effectively
		presenter.set("PM Teaching Methods Used Effectively", pmtm) #7
		
		jmks = presenter.rangefield('N-17', 0, 4) #Julia MacMillan Knowledge Subject
		presenter.set("JM Knowledge of Subject", jmks) #8
		
		jmop = presenter.rangefield('N-18', 0, 4) #Julia MacMillan Organized in Presenting
		presenter.set("JM Organized in Presenting", jmop) #9
		
		jmcd = presenter.rangefield('N-19', 0, 4) #Julia MacMillan Effective in Content Delivery
		presenter.set("JM Effective in Content Delivery", jmcd) #10
		
		jmtm = presenter.rangefield('N-20', 0, 4) #Julia MacMillan Teaching Methods Used Effectively
		presenter.set("JM Teaching Methods Used Effectively", jmtm) #11
		
		tkks = presenter.rangefield('AD-17', 0, 4) #Tara Kelly Knowledge Subject
		presenter.set("TK Knowledge of Subject", tkks) #12
		
		tkop = presenter.rangefield('AD-18', 0, 4) #Tara Kelly Organized in Presenting
		presenter.set("TK Organized in Presenting", tkop) #13
		
		tkcd = presenter.rangefield('AD-19', 0, 4) #Tara Kelly Effective in Content Delivery
		presenter.set("TK Effective in Content Delivery", tkcd) #14
		
		tktm = presenter.rangefield('AD-20', 0, 4) #Tara Kelly Teaching Methods Used Effectively
		presenter.set("TK Teaching Methods Used Effectively", tktm) #15
		
	  ebks = presenter.rangefield('V-23', 0, 4) #Emily Bialy Knowledge Subject
		presenter.set("EB Knowledge of Subject", ebks) #16
		
		ebop = presenter.rangefield('V-24', 0, 4) #Emily Bialy Organized in Presenting
		presenter.set("EB Organized in Presenting", ebop) #17
		
		ebcd = presenter.rangefield('V-25', 0, 4) #Emily Bialy Effective in Content Delivery
		presenter.set("EB Effective in Content Delivery", ebcd) #18
		
		ebtm = presenter.rangefield('V-26', 0, 4) #Emily Bialy Teaching Methods Used Effectively
		presenter.set("EB Teaching Methods Used Effectively", ebtm) #19
		
		self1 = presenter.rangefield('AA-34', 0, 4) #Self Eval 1
		presenter.set("Communication", self1) #20
		
		self2 = presenter.rangefield('AA-35', 0, 4) #Self Eval 2
		presenter.set("Ethics", self2) #21
		
		self3 = presenter.rangefield('AA-36', 0, 4) #Self Eval 3
		presenter.set("Advocacy", self3) #22
		
		self4 = presenter.rangefield('AA-37', 0, 4) #Self Eval 4
		presenter.set("Objectives relation to purpose of educational activity", self4) #23
		
		num1 = presenter.rangefield('M-39', 0, 1)
		if num1 == 0:
		  bias = "No"
		elif num1 == 1:
		  bias = "Yes"
		presenter.set("Bias", bias)) #24

		presenter.submit()

# This line creates a new Pipresenter and starts the program
# It takes the main function as an argument and runs it when it finds a new sheet
Pipresenter(main)
