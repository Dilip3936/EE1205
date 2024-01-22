#include <stdio.h>
#include <math.h>

int main() {
    FILE *file = fopen("data.txt", "w");
    if (file == NULL) {
        printf("Error opening file\n");
        return 1;
    }

    double a = -2.0 / 7.0;
    double r1 = -7.0 / 2.0;
    double r2 = 7.0 / 2.0;

    for (int n = 0; n < 10; n++) {
        double y1 = a * pow(r1, n);
        double y2 = a * pow(r2, n);
        fprintf(file, "%d %f %f\n", n, y1, y2);
    }

    fclose(file);
    return 0;
}
