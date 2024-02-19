import os
import sys
import time
import subprocess

system_os = sys.platform  # Définir le système d'exploitation
file_name = sys.argv[0]  # Définir le nom du fichier


def print_rgb(r, g, b, texte):
  print(f"\x1b[38;2;{r};{g};{b}m{texte}\x1b[0m", end='')


def linux():
  os.system("clear")


def windows():
  os.system("cls")


def main():
  if system_os == "linux":
    linux()
  else:
    windows()

  print_rgb(255, 255, 255, "[")
  print_rgb(255, 105, 180, "?")
  print_rgb(255, 255, 255, "] Drag file here >>>")
  path = input(" ").strip()
  path_check = path[1:3]

  if path_check == ":\\":
    print_rgb(255, 255, 255, "[")
    print_rgb(50, 255, 50, "+")
    print_rgb(255, 255, 255, f"] File : {path}")
    print("")
    time.sleep(0.5)
    print_rgb(255, 255, 255, "[")
    print_rgb(255, 105, 180, "?")
    print_rgb(255, 255, 255, "] Which year the file should be >>>")
    year = int(input(" "))

    if year < 1970:
      print_rgb(255, 255, 255, "[")
      print_rgb(255, 50, 50, "!")
      print_rgb(
          255, 255, 255,
          "] Year must not be below 1970. Programe will restart press any key."
      )
      input(" ")
      os.system(f"python {file_name}")
    else:
      time.sleep(0.5)
      print_rgb(255, 255, 255, "[")
      print_rgb(255, 105, 180, "?")
      print_rgb(255, 255, 255, "] Which month the file should be >>>")
      month = int(input(" "))

      if month < 1 or month > 12:
        print_rgb(255, 255, 255, "[")
        print_rgb(255, 50, 50, "!")
        print_rgb(
            255, 255, 255,
            "] Month must be between 1 and 12. Programe will restart press any key."
        )
        input(" ")
        os.system(f"python {file_name}")
      else:
        time.sleep(0.5)
        print_rgb(255, 255, 255, "[")
        print_rgb(255, 105, 180, "?")
        print_rgb(255, 255, 255, "] Which day the file should be >>>")
        day = int(input(" "))
        if day < 1 or day > 31:
          print_rgb(255, 255, 255, "[")
          print_rgb(255, 50, 50, "!")
          print_rgb(
              255, 255, 255,
              "] Day must be between 1 and 31. Programe will restart press any key."
          )
          input(" ")
          os.system(f"python {file_name}")
        elif day == 31 and month == 2 or day == 31 and month == 4 or day == 31 and month == 6 or day == 31 and month == 9 or day == 31 and month == 11:
          print_rgb(255, 255, 255, "[")
          print_rgb(255, 50, 50, "!")
          print_rgb(
              255, 255, 255,
              "] Day must not be 31. Programe will restart press any key.")
          input(" ")
          os.system(f"python {file_name}")
        elif day == 30 and month == 2:
          print_rgb(255, 255, 255, "[")
          print_rgb(255, 50, 50, "!")
          print_rgb(
              255, 255, 255,
              "] Day must not be 30. Programe will restart press any key.")
          input(" ")
          os.system(f"python {file_name}")
        elif day == 29 and month == 2 and year % 4 != 0:
          print_rgb(255, 255, 255, "[")
          print_rgb(255, 50, 50, "!")
          print_rgb(
              255, 255, 255,
              "] Day must not be 29. Programe will restart press any key.")
          input(" ")
          os.system(f"python {file_name}")
        else:
          print_rgb(255, 255, 255, "[")
          print_rgb(50, 255, 50, "+")
          print_rgb(255, 255, 255, f"] Date : {day}/{month}/{year}")
          print("")
          time.sleep(0.5)
          print_rgb(255, 255, 255, "[")
          print_rgb(255, 105, 180, "?")
          print_rgb(255, 255, 255, "] Which hour the file should be >>>")
          hours = int(input(" "))
          if hours < 0 or hours > 23:
            print_rgb(255, 255, 255, "[")
            print_rgb(255, 50, 50, "!")
            print_rgb(
                255, 255, 255,
                "] Hour must be between 0 and 23. Programe will restart press any key."
            )
            input(" ")
            os.system(f"python {file_name}")
          else:
            time.sleep(0.5)
            print_rgb(255, 255, 255, "[")
            print_rgb(255, 105, 180, "?")
            print_rgb(255, 255, 255, "] Which minute the file should be >>>")
            minutes = int(input(" "))
            if minutes < 0 or minutes > 59:
              print_rgb(255, 255, 255, "[")
              print_rgb(255, 50, 50, "!")
              print_rgb(
                  255, 255, 255,
                  "] Minutes must be between 0 and 59. Programe will restart press any key."
              )
              input(" ")
              os.system(f"python {file_name}")
            else:
              time.sleep(0.5)
              print_rgb(255, 255, 255, "[")
              print_rgb(255, 105, 180, "?")
              print_rgb(255, 255, 255, "] Which second the file should be >>>")
              seconds = int(input(" "))
              if seconds < 0 or seconds > 59:
                print_rgb(255, 255, 255, "[")
                print_rgb(255, 50, 50, "!")
                print_rgb(
                    255, 255, 255,
                    "] Second must be between 0 and 59. Programe will restart press any key."
                )
                input(" ")
                os.system(f"python {file_name}")
              else:
                time.sleep(0.5)
                print_rgb(255, 255, 255, "[")
                print_rgb(50, 255, 50, "+")
                print_rgb(255, 255, 255,
                          f"] Time : {hours}:{minutes}:{seconds}")
                print("")
                time.sleep(0.5)
                print_rgb(255, 255, 255, "[")
                print_rgb(138, 43, 226, "1")
                print_rgb(255, 255, 255, "] ")
                print_rgb(138, 43, 226, "Modify just Creation time")
                print("")

                print_rgb(255, 255, 255, "[")
                print_rgb(255, 140, 0, "2")
                print_rgb(255, 255, 255, "] ")
                print_rgb(255, 140, 0, "Modify just Last write time")
                print("")

                print_rgb(255, 255, 255, "[")
                print_rgb(0, 250, 154, "3")
                print_rgb(255, 255, 255, "] ")
                print_rgb(0, 250, 154, "Modify just Last acces time")
                print("")

                print_rgb(255, 255, 255, "[")
                print_rgb(160, 82, 45, "4")
                print_rgb(255, 255, 255, "] ")
                print_rgb(160, 82, 45, "Modify all")
                print("")

                print_rgb(255, 255, 255, "[")
                print_rgb(255, 105, 180, "?")
                print_rgb(255, 255, 255, "] Which mode should be >>>")
                mode = int(input(" "))
                if mode == 1:
                  powershell_command_creation = f'$(get-item {path}).CreationTime = (Get-Date("{year}-{month}-{day} {hours}:{minutes}:{seconds}"))'
                  subprocess.run(
                      ['powershell', '-Command', powershell_command_creation],
                      check=True)
                  print_rgb(255, 255, 255, "[")
                  print_rgb(50, 255, 50, "+")
                  print_rgb(255, 255, 255, "] Creation time modified")
                  input(" ")
                elif mode == 2:
                  powershell_command_last_write = f'$(get-item {path}).LastWriteTime = (Get-Date("{year}-{month}-{day} {hours}:{minutes}:{seconds}"))'
                  subprocess.run([
                      'powershell', '-Command', powershell_command_last_write
                  ],
                                 check=True)
                  print_rgb(255, 255, 255, "[")
                  print_rgb(50, 255, 50, "+")
                  print_rgb(255, 255, 255, "] Last write time modified")
                  input(" ")
                elif mode == 3:
                  powershell_command_last_acces = f'$(get-item {path}).LastAccessTime  = (Get-Date("{year}-{month}-{day} {hours}:{minutes}:{seconds}"))'
                  subprocess.run([
                      'powershell', '-Command', powershell_command_last_acces
                  ],
                                 check=True)
                  print_rgb(255, 255, 255, "[")
                  print_rgb(50, 255, 50, "+")
                  print_rgb(255, 255, 255, "] Last time acces modified")
                  input(" ")
                elif mode == 4:
                  powershell_command_creation = f'$(get-item {path}).CreationTime = (Get-Date("{year}-{month}-{day} {hours}:{minutes}:{seconds}"))'
                  subprocess.run(
                      ['powershell', '-Command', powershell_command_creation],
                      check=True)
                  powershell_command_last_write = f'$(get-item {path}).LastWriteTime = (Get-Date("{year}-{month}-{day} {hours}:{minutes}:{seconds}"))'
                  subprocess.run([
                      'powershell', '-Command', powershell_command_last_write
                  ],
                                 check=True)
                  powershell_command_last_acces = f'$(get-item {path}).LastAccessTime  = (Get-Date("{year}-{month}-{day} {hours}:{minutes}:{seconds}"))'
                  subprocess.run([
                      'powershell', '-Command', powershell_command_last_acces
                  ],
                                 check=True)
                  print_rgb(255, 255, 255, "[")
                  print_rgb(50, 255, 50, "+")
                  print_rgb(255, 255, 255, "] All information modified")
                  input(" ")
                else:
                  print_rgb(255, 255, 255, "[")
                  print_rgb(255, 50, 50, "!")
                  print_rgb(
                      255, 255, 255,
                      "] Mode must be between 0 and 4. Programe will restart press any key."
                  )
                  input(" ")
                  os.system(f"python {file_name}")

  else:
    print_rgb(255, 255, 255, "[")
    print_rgb(255, 50, 50, "!")
    print_rgb(255, 255, 255,
              "] File not found. Programe will restart press any key.")
    input(" ")
    os.system(f"python {file_name}")


if __name__ == "__main__":
  main()
