
int power (int n)
{
    int answer = 1;
    
    while(n)
    {
        answer *= 3;
        n--;
    }
    return answer;
}

int solution(int n)
{
    int answer = 0;
    int n3digit = 0;
    int n10digit = 0;
    
    int an3bit[30] = {0, };
    
    while(n)
    {
        an3bit[n3digit] = n % 3;
        n /= 3;
        n3digit++;
    }

    while(n3digit)
    {
        answer = power(n3digit - 1) * an3bit[n10digit] + answer;
        n10digit++;
        n3digit--;
    }
    
    return answer;
}