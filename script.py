
import sys
import os 

DRY_RUN = True

def process_files(input_folder: str, output_folder: str, fuzz_command: str, tmin_path: str) -> None:

	input_files = os.listdir(input_folder)

	# Make directories end in "/"
	if input_folder[-1] != "/":
		input_folder += "/"
	if output_folder[-1] != "/":
		output_folder += "/"

	for i, file in enumerate(input_files):

		# Now actually run afl-tmin .

		# afl-tmin -i INPUTDIR/INPUTFILE -o OUTPUTDIR/OUTPUTFILE -- COMMAND

		final_command = tmin_path+" -i "+input_folder+file+" -o "+output_folder+file+".minimized -- "+fuzz_command

		

		if not DRY_RUN:
			print("Now running : "+str(final_command))
			os.system(final_command)

		else:
			print("Dry run. Command would have been this: : "+str(final_command))


	return 0


def print_help() -> None:
	print("Usage: python3 "+str(sys.argv[0])+" -i INPUTFOLDER -o OUTPUTFOLDER -c \"FUZZING COMMAND\" -t \"AFL-TMIN PATH\"")

def arg_helper(argument):

	return sys.argv[sys.argv.index(argument)+1]

def process_arguments() -> tuple:

	if "-i" not in sys.argv or "-o" not in sys.argv or "-c" not in sys.argv or "-t" not in sys.argv:
		print_help()
		return None

	indir = arg_helper("-i")
	outdir = arg_helper("-o")
	command = arg_helper("-c")
	tmin_path = arg_helper("-t")

	return indir, outdir, command, tmin_path


def main() -> int:

	if "--help" in sys.argv:
		print_help()
		return 0

	if len(sys.argv) != 9:
		print_help()
		return 1

	indir, outdir, command, tmin_path = process_arguments()

	if indir == None:
		return 1

	ret = process_files(indir, outdir, command, tmin_path)


	return ret


if __name__=="__main__":

	exit(main())
