#include <iostream>
using namespace std;
char board[3][3] = {{'1', '2', '3'}, {'4', '5', '6'}, {'7', '8', '9'}};
int choice;
int row, column;
char turn = 'X';
bool draw = false;
string n1;
string n2;

void display_board()
{
    system("cls"); // use "cls" on windows
    cout << n1 << " [X] " << n2 << " [O] \n\n";
    cout << "     |     |     \n";
    cout << "  " << board[0][0] << "  |  " << board[0][1] << "  |  " << board[0][2] << " \n";
    cout << "_____|_____|_____\n";
    cout << "     |     |     \n";
    cout << "  " << board[1][0] << "  |  " << board[1][1] << "  |  " << board[1][2] << " \n";
    cout << "_____|_____|_____\n";
    cout << "     |     |     \n";
    cout << "  " << board[2][0] << "  |  " << board[2][1] << "  |  " << board[2][2] << " \n";
    cout << "     |     |     \n";
}

void player_turn()
{
    if (turn == 'X')
    {
        cout << n1 << " [X] turn : ";
    }
    else if (turn == 'O')
    {
        cout << n2 << "[O] turn : ";
    }
    cin >> choice;

    if (choice == 1)
    {
        row = 0;
        column = 0;
    }
    else if (choice == 2)
    {
        row = 0;
        column = 1;
    }
    else if (choice == 3)
    {
        row = 0;
        column = 2;
    }
    else if (choice == 4)
    {
        row = 1;
        column = 0;
    }
    else if (choice == 5)
    {
        row = 1;
        column = 1;
    }
    else if (choice == 6)
    {
        row = 1;
        column = 2;
    }
    else if (choice == 7)
    {
        row = 2;
        column = 0;
    }
    else if (choice == 8)
    {
        row = 2;
        column = 1;
    }
    else if (choice == 9)
    {
        row = 2;
        column = 2;
    }
    else
    {
        cout << "Invalid Move";
    }

    if (turn == 'X' && board[row][column] != 'X' && board[row][column] != 'O')
    {
        board[row][column] = 'X';
        turn = 'O';
    }
    else if (turn == 'O' && board[row][column] != 'X' && board[row][column] != 'O')
    {
        board[row][column] = 'O';
        turn = 'X';
    }
    else
    {
        cout << "Box already filled!\n Please try again!!\n\n";
        player_turn();
    }

    display_board();
}

bool gameover()
{
    // check win
    for (int i = 0; i < 3; i++)
        if (board[i][0] == board[i][1] && board[i][0] == board[i][2] || board[0][i] == board[1][i] && board[0][i] == board[2][i])
            return false;

    if (board[0][0] == board[1][1] && board[0][0] == board[2][2] || board[0][2] == board[1][1] && board[0][2] == board[2][0])
        return false;

    // if there is any box not filled
    for (int i = 0; i < 3; i++)
        for (int j = 0; j < 3; j++)
            if (board[i][j] != 'X' && board[i][j] != 'O')
                return true;

    // draw
    draw = true;
    return false;
}

int main()
{
    cout << "TIC TAC TOE GAME\n";
    cout << "For 2 players\n";
    cout << "enter the first player name: ";
    getline(cin, n1);
    cout << "enter the second player name: ";
    getline(cin, n2);
    while (gameover())
    {
        display_board();
        player_turn();
        gameover();
    }
    if (turn == 'X' && draw == false)
    {
        cout << n2 << "[O] Wins!! Congratulations\n";
    }
    else if (turn == 'O' && draw == false)
    {
        cout << n1 << " [X] Wins!! Congratulations\n";
    }
    else
        cout << "GAME DRAW!!!\n";
}
