import hashlib

# Your details
details = {
    "name": "Joy Mondal",
    "github": "https://github.com/codewithjoymondal",
    "youtube": "https://www.youtube.com/@CodeWithJoy",
    "Linkedin" : "https://www.linkedin.com/in/codewithjoymondal"
}

c_programs = {
    1: '''// DDA Line Drawing Algorithm
#include <graphics.h>
#include <conio.h>
#include <stdio.h>

int main() {
    int gd = DETECT, gm, i;
    float x, y, dx, dy, steps;
    int x0, x1, y0, y1;

    initgraph(&gd, &gm, "C:\\TC\\BGI");
    setbkcolor(WHITE);

    x0 = 100, y0 = 200, x1 = 500, y1 = 300;
    dx = (float)(x1 - x0);
    dy = (float)(y1 - y0);

    if (dx >= dy) {
        steps = dx;
    } else {
        steps = dy;
    }

    dx = dx / steps;
    dy = dy / steps;
    x = x0;
    y = y0;
    i = 1;

    while (i <= steps) {
        putpixel(x, y, RED);
        x += dx;
        y += dy;
        i = i + 1;
    }

    getch();
    closegraph();
    return 0; // Adding a return statement with an integer value
} ''',
2: '''// Bresenham's Line Drawing Algorithm
#include<iostream>
#include<graphics.h>

using namespace std;

void drawline(int x0, int y0, int x1, int y1) {
    int dx, dy, p, x, y;

    dx = x1 - x0;
    dy = y1 - y0;

    x = x0;
    y = y0;

    p = 2 * dy - dx;

    while (x <= x1) {
        putpixel(x, y, 7);

        if (p >= 0) {
            y = y + 1;
            p = p + 2 * (dy - dx);
        } else {
            p = p + 2 * dy;
        }
        x = x + 1;
    }
}

int main() {
    int gdriver = DETECT, gmode, error, x0, y0, x1, y1;
    initgraph(&gdriver, &gmode, "c:\\turboc3\\bgi");

    cout << "Enter co-ordinates of first point: ";
    cin >> x0 >> y0;

    cout << "Enter co-ordinates of second point: ";
    cin >> x1 >> y1;

    drawline(x0, y0, x1, y1);

    getch();
    closegraph();
    return 0;
} ''',
3: '''// Bresenham's Circle Drawing Algorithm
#include<graphics.h>
#include<conio.h>
#include<graphics.h>
#include<math.h>
int main()
{
    int gd = DETECT, gm;
    initgraph(&gd,&gm, "");
    int xc, yc, x,y,d,r;
    printf("Enter the center of the circle");
    scanf("%d %d", &xc, &yc);
    printf("Enter the radius of the circle:");
    scanf("%d", &r);
    x = 0, y = r;
    d = 3 - 2 * r;
    while(x<=y)
    {
        putpixel(xc + x, yc + y,WHITE);
        putpixel(xc + y, yc + x,WHITE);
        putpixel(xc + x, yc - y,WHITE);
        putpixel(xc + y, yc - x,WHITE);
        putpixel(xc - x, yc - y,WHITE);
        putpixel(xc - y, yc - x,WHITE);
        putpixel(xc - x, yc + y,WHITE);
        putpixel(xc - y, yc + x,WHITE);
        x = x + 1;
        if (d < 0)
        {
          d=d+(4*x)+6;
        }
        else
        {
            y = y -1;
            d = d + 4*(x-y)+10;
        }


    }
    getch();
    closegraph();
} ''',
4: '''// Midpoint Circle Drawing Algorithm
#include<stdio.h>
#include<graphics.h>
#include<math.h>
#include<conio.h>

int main()
{
    int gd = DETECT, gm;
    initgraph(&gd, &gm, "");
    int xc, yc, x, y, d, r;
    printf(" Enter the center of the circle:");
    scanf("%d %d", &xc, &yc);
    printf("Enter the radius:");
    scanf("%d", &r);

    x =0, y = r;
    d = 1-r;
    while(x<=y)
    {
        putpixel(xc+x, yc+y, RED);
        putpixel(xc+y, yc+x, RED);
        putpixel(xc+x, yc-y, RED);
        putpixel(xc+y, yc-x, RED);
        putpixel(xc-x, yc-y, RED);
        putpixel(xc-y, yc-x, RED);
        putpixel(xc-x, yc+y, RED);
        putpixel(xc-y, yc+x, RED);

        x = x+1;

        if(d<0)
        {
            d = d+ 2*x + 3;
        }
        else
        {
            y = y-1;
            d = d+ 2*(x-y) + 5;
        }
    }
    getch();
    closegraph();
}
 ''',
5: '''// Flood Fill Algorithm with 4-connected method
#include <iostream>
#include <graphics.h>

void floodFill4(int x, int y, int fillColor, int oldColor) {
    if (getpixel(x, y) == oldColor) {
        putpixel(x, y, fillColor);
        floodFill4(x + 1, y, fillColor, oldColor);
        floodFill4(x - 1, y, fillColor, oldColor);
        floodFill4(x, y + 1, fillColor, oldColor);
        floodFill4(x, y - 1, fillColor, oldColor);
    }
}

int main() {
    int gd = DETECT, gm;
    initgraph(&gd, &gm, "");

    // Draw a boundary
    rectangle(50, 50, 200, 150);

    // Coordinates to start the flood fill
    int x = 100, y = 100;
    int fillColor = RED; // Color to fill
    int oldColor = getpixel(x, y); // Get the color of the starting pixel

    floodFill4(x, y, fillColor, oldColor);

    getch();
    closegraph();

    return 0;
} ''',
6: '''// Flood Fill Algorithm with 8-connected method
#include <iostream>
#include <graphics.h>

void floodFill8(int x, int y, int fillColor, int oldColor) {
    if (getpixel(x, y) == oldColor) {
        putpixel(x, y, fillColor);
        floodFill8(x + 1, y, fillColor, oldColor);
        floodFill8(x - 1, y, fillColor, oldColor);
        floodFill8(x, y + 1, fillColor, oldColor);
        floodFill8(x, y - 1, fillColor, oldColor);
        floodFill8(x + 1, y + 1, fillColor, oldColor);
        floodFill8(x + 1, y - 1, fillColor, oldColor);
        floodFill8(x - 1, y + 1, fillColor, oldColor);
        floodFill8(x - 1, y - 1, fillColor, oldColor);
    }
}

int main() {
    int gd = DETECT, gm;
    initgraph(&gd, &gm, "");

    // Draw a boundary
    rectangle(50, 50, 200, 150);

    // Coordinates to start the flood fill
    int x = 100, y = 100;
    int fillColor = GREEN; // Color to fill
    int oldColor = getpixel(x, y); // Get the color of the starting pixel

    floodFill8(x, y, fillColor, oldColor);

    getch();
    closegraph();

    return 0;
} ''',
7: '''// Boundary Fill Algorithm with 4-connected method
#include <iostream>
#include <graphics.h>

void boundaryFill4(int x, int y, int fillColor, int borderColor) {
    if (getpixel(x, y) != borderColor && getpixel(x, y) != fillColor) {
        putpixel(x, y, fillColor);
        boundaryFill4(x + 1, y, fillColor, borderColor);
        boundaryFill4(x - 1, y, fillColor, borderColor);
        boundaryFill4(x, y + 1, fillColor, borderColor);
        boundaryFill4(x, y - 1, fillColor, borderColor);
    }
}

int main() {
    int gd = DETECT, gm;
    initgraph(&gd, &gm, "");

    // Draw a boundary
    rectangle(50, 50, 200, 150);

    // Coordinates to start the boundary fill
    int x = 100, y = 100;
    int fillColor = BLUE; // Color to fill
    int borderColor = WHITE; // Boundary color

    boundaryFill4(x, y, fillColor, borderColor);

    getch();
    closegraph();

    return 0;
} ''',
8: '''// Boundary Fill Algorithm with 8-connected method
#include <iostream>
#include <graphics.h>

void boundaryFill8(int x, int y, int fillColor, int borderColor) {
    if (getpixel(x, y) != borderColor && getpixel(x, y) != fillColor) {
        putpixel(x, y, fillColor);
        boundaryFill8(x + 1, y, fillColor, borderColor);
        boundaryFill8(x - 1, y, fillColor, borderColor);
        boundaryFill8(x, y + 1, fillColor, borderColor);
        boundaryFill8(x, y - 1, fillColor, borderColor);
        boundaryFill8(x + 1, y + 1, fillColor, borderColor);
        boundaryFill8(x + 1, y - 1, fillColor, borderColor);
        boundaryFill8(x - 1, y + 1, fillColor, borderColor);
        boundaryFill8(x - 1, y - 1, fillColor, borderColor);
    }
}

int main() {
    int gd = DETECT, gm;
    initgraph(&gd, &gm, "");

    // Draw a boundary
    rectangle(50, 50, 200, 150);

    // Coordinates to start the boundary fill
    int x = 100, y = 100;
    int fillColor = BLUE; // Color to fill
    int borderColor = WHITE; // Boundary color

    boundaryFill8(x, y, fillColor, borderColor);

    getch();
    closegraph();

    return 0;
}  ''',
9: '''// Scan Line Polygon Fill Algorithm
#include <iostream>
#include <graphics.h>
#include <vector>
#include <algorithm>

struct Point { int x, y; };

void scanLineFill(const std::vector<Point>& points, int fillColor) {
    int minY = INT_MAX, maxY = 0;
    for (const auto& point : points) {
        minY = std::min(minY, point.y);
        maxY = std::max(maxY, point.y);
    }

    for (int y = minY + 1; y < maxY; ++y) {
        std::vector<int> intersections;
        size_t n = points.size();

        for (size_t i = 0; i < n; ++i) {
            int j = (i + 1) % n;
            int x1 = points[i].x, y1 = points[i].y;
            int x2 = points[j].x, y2 = points[j].y;

            if ((y >= y1 && y < y2) || (y >= y2 && y < y1)) {
                if (y2 - y1 != 0) {
                    int x = (int)(((x2 - x1) * (y - y1)) / (float)(y2 - y1) + x1);
                    intersections.push_back(x);
                }
            }
        }

        std::sort(intersections.begin(), intersections.end());
        for (size_t i = 0; i < intersections.size(); i += 2) {
            for (int x = intersections[i] + 1; x < intersections[i + 1]; ++x) {
                putpixel(x, y, fillColor);
            }
        }
    }
}

int main() {
    int gd = DETECT, gm;
    initgraph(&gd, &gm, "");

    std::vector<Point> points = { {100, 100}, {200, 50}, {300, 100}, {250, 200}, {150, 200} };
    int fillColor = GREEN;

    for (size_t i = 0; i < points.size(); ++i) {
        size_t j = (i + 1) % points.size();
        line(points[i].x, points[i].y, points[j].x, points[j].y);
    }

    scanLineFill(points, fillColor);

    getch();
    closegraph();

    return 0;
} '''
}

def hash_password(password):
    hashed = hashlib.sha256(password.encode()).hexdigest()
    return hashed

def authenticate(password):
    stored_password = "9ec35248623fcdf75f7dc876ed17f540f9f15dce6127266624b14279b97b009f" 
    entered_password = hash_password(password)
    return entered_password == stored_password

def display_program_names():
    print("Available C++ programming codes:")
    for serial_number, code in c_programs.items():
        print(f"{serial_number}. {code.splitlines()[0]}")

def display_c_program(serial_number, password):
    if authenticate(password):
        if serial_number in c_programs:
            print(f"\nCode for C++ Program {serial_number}:\n")
            print(c_programs[serial_number])
            program_name = c_programs[serial_number].splitlines()[0]
            filename = ''.join(e for e in program_name if e.isalnum() or e in (' ', '_')).rstrip()
            with open(f'{filename}.cpp', 'w') as f:
                f.write(c_programs[serial_number])
        else:
            print("Invalid serial number. Please enter a valid serial number.")
    else:
        print("Invalid password. Access denied.")

password = input("Enter the password to view the C++ programs: ")

if authenticate(password):
    display_program_names()
    serial = int(input("\nEnter the serial number of the C++ program to view (1-9): "))
    display_c_program(serial, password)
    print("\nDevloper information:")
    for key, value in details.items():
        print(f"{key.capitalize()}: {value}")
else:
    print("Invalid password. Access denied.")
