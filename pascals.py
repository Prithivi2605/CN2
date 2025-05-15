#server.py
import socket

def generatePascal(n):
    triangle = []
    for i in range(n):
        row = [1]
        if i > 0:
            prev = triangle[i - 1]
            for j in range(1, i):  # Fix loop range and append sums
                row.append(prev[j - 1] + prev[j])
            row.append(1)
        triangle.append(row)
    return triangle

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(('127.0.0.1', 8080))


print("Server is Running")

data,add = server.recvfrom(1024) # Missing parentheses to call decode()

row = int(data.decode())

triangle = generatePascal(row)

# Convert each row to a string and join rows with newline for better formatting
triangle_str = "\n".join(" ".join(map(str, r)) for r in triangle)

server.sendto(triangle_str.encode(),add)

server.close()


#client.py
import socket

client=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)


row=int(input('Enter no of rows'))
client.sendto(str(row).encode(),('127.0.0.1',8080))

data,_=client.recvfrom(4096)
triangle=data.decode()
print(triangle)