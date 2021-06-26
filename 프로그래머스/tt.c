void draw1(int h)
{
    if (h == 0)
    {
        return;
    }
    draw1(h - 1);
    for (int i = 0; i < h; i++)
    {
        printf("*");
    }
    printf("\n");
}

draw1(5);