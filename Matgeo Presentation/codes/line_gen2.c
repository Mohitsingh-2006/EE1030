     return 1;
    }

    // Calculate 100 points on the circle
    for (int i = 0; i < num_points; i++) {
        // Calculate angle (theta) for current point
        theta = 2 * PI * i / num_points;

        // Parametric equations of a circle
        x = r * cos(theta);
        y = r * sin(theta) + center_y;

        // Print the points to the file
        fprintf(file, "%lf %lf\n", x, y);
    }

    // Close the file
    fclose(file);

    printf("100 points on the circle have been saved to circle_points.dat.\n");
    return 0;
}

