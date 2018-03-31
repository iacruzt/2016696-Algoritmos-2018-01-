results = studyInsertionSort(10, False)

distribution = list(np.bincount(results[1]))
plotter.bar([distribution.index(x) for x in distribution],distribution,width=15)
plotter.xlabel("# of instructions.")
plotter.ylabel("# of permutations")
plotter.title("Distribution of the number of instructions\n along a sample of permutations")
plotter.show()

distribution = list(np.bincount(results[3]))
plotter.bar([distribution.index(x) for x in distribution],distribution,width=15)
plotter.xlabel("# of comparisons.")
plotter.ylabel("# of permutations")
plotter.title("Distribution of the number of comparisons\n along a sample of permutations")
plotter.show()

distribution = list(np.bincount(results[5]))
plotter.bar([distribution.index(x) for x in distribution],distribution,width=15)
plotter.xlabel("# of swaps.")
plotter.ylabel("# of permutations")
plotter.title("Distribution of the number of swaps along \n a sample of permutations")
plotter.show()

print("AVG instructions count {0} | AVG comparisons count {1} | AVG Instructions count {2}".format 
      (results[0], results[2], results[4]))
