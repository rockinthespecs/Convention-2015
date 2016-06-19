from panel import * #What does this do?

# Main method to process a full-page sheet
# Submits three times, because there are three matches on one sheet
def main(panel):
	for s in (0,16,32): #What the heck does this mean?
	  panel.shiftDown(s)

		# The numberings of the fields are important; you reference them by number in server.py
		bkks = panel.countfield('N-11', 0, 4) #Barbara Katz Knowledge Subject
		panel.set("BK Knowledge of Subject", bkks) #0
		
		bkop = panel.countfield('N-12', 0, 4) #Barbara Katz Organized in Presenting
		panel.set("BK Organized in Presenting", bkop) #1
		
		bkcd = panel.countfield('N-13', 0, 4) #Barbara Katz Effective in Content Delivery
		panel.set("BK Effective in Content Delivery", bkcd) #2
		
		bktm = panel.countfield('N-14', 0, 4) #Barbara Katz Teaching Methods Used Effectively
		panel.set("BK Teaching Methods Used Effectively", bktm) #3
		
		pmks = panel.countfield('AD-11', 0, 4) #Pamela D. Miller Knowledge Subject
		panel.set("PM Knowledge of Subject", pmks) #4
		
		pmop = panel.countfield('AD-12', 0, 4) #Pamela D. Miller Organized in Presenting
		panel.set("PM Organized in Presenting", pmop) #5
		
		pmcd = panel.countfield('AD-13', 0, 4) #Pamela D. Miller Effective in Content Delivery
		panel.set("PM Effective in Content Delivery", pmcd) #6
		
		pmtm = panel.countfield('AD-14', 0, 4) #Pamela D. Miller Teaching Methods Used Effectively
		panel.set("PM Teaching Methods Used Effectively", pmtm) #7
		
		jmks = panel.countfield('N-17', 0, 4) #Julia MacMillan Knowledge Subject
		panel.set("JM Knowledge of Subject", jmks) #8
		
		jmop = panel.countfield('N-18', 0, 4) #Julia MacMillan Organized in Presenting
		panel.set("JM Organized in Presenting", jmop) #9
		
		jmcd = panel.countfield('N-19', 0, 4) #Julia MacMillan Effective in Content Delivery
		panel.set("JM Effective in Content Delivery", jmcd) #10
		
		jmtm = panel.countfield('N-20', 0, 4) #Julia MacMillan Teaching Methods Used Effectively
		panel.set("JM Teaching Methods Used Effectively", jmtm) #11
		
		tkks = panel.countfield('AD-17', 0, 4) #Tara Kelly Knowledge Subject
		panel.set("TK Knowledge of Subject", tkks) #12
		
		tkop = panel.countfield('AD-18', 0, 4) #Tara Kelly Organized in Presenting
		panel.set("TK Organized in Presenting", tkop) #13
		
		tkcd = panel.countfield('AD-19', 0, 4) #Tara Kelly Effective in Content Delivery
		panel.set("TK Effective in Content Delivery", tkcd) #14
		
		tktm = panel.countfield('AD-20', 0, 4) #Tara Kelly Teaching Methods Used Effectively
		panel.set("TK Teaching Methods Used Effectively", tktm) #15
		
	  ebks = panel.countfield('V-23', 0, 4) #Emily Bialy Knowledge Subject
		panel.set("EB Knowledge of Subject", ebks) #16
		
		ebop = panel.countfield('V-24', 0, 4) #Emily Bialy Organized in Presenting
		panel.set("EB Organized in Presenting", ebop) #17
		
		ebcd = panel.countfield('V-25', 0, 4) #Emily Bialy Effective in Content Delivery
		panel.set("EB Effective in Content Delivery", ebcd) #18
		
		ebtm = panel.countfield('V-26', 0, 4) #Emily Bialy Teaching Methods Used Effectively
		panel.set("EB Teaching Methods Used Effectively", ebtm) #19
		
		self1 = panel.countfield('AA-34', 0, 4) #Self Eval 1
		panel.set("Communication", self1) #20
		
		self2 = panel.countfield('AA-35', 0, 4) #Self Eval 2
		panel.set("Ethics", self2) #21
		
		self3 = panel.countfield('AA-36', 0, 4) #Self Eval 3
		panel.set("Advocacy", self3) #22
		
		self4 = panel.countfield('AA-37', 0, 4) #Self Eval 4
		panel.set("Objectives relation to purpose of educational activity", self4) #23
		
		num1 = panel.countfield('M-39', 0, 1)
		if num1 == 0:
		  bias = "No"
		elif num1 == 1:
		  bias = "Yes"
		panel.set("Bias", bias)) #24

		panel.submit()

# This line creates a new Pipanel and starts the program
# It takes the main function as an argument and runs it when it finds a new sheet
Pipanel(main)
