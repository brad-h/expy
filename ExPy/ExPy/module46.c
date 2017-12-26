#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <assert.h>

// A naive implementation that uses a linked list
// instead of a dictionary to look up the values
typedef struct Counter {
    const char* word;
    int frequency;
} Counter;

typedef struct Node {
    void* this;
    struct Node* next;
} Node;

// https://en.wikipedia.org/wiki/Merge_sort#Top-down_implementation_using_lists

Node* create_counter(const char * word) {
    Counter* counter = malloc(sizeof(Counter));
    counter->word = word;
    counter->frequency = 1;
    Node* node = malloc(sizeof(Node));
    node->this = counter;
    node->next = NULL;
    return node;
}

void bump(Node* root, const char * word) {
    assert(root != NULL);
    Node* node = root;
    Node* last = root->next;
    while (node != NULL) {
        Counter* counter = node->this;
        if (strcmp(counter->word, word) == 0) {
            counter->frequency++;
            return;
        }
        last = node;
        node = node->next;
    }
    last->next = create_counter(word);
}

int descending(const void* left_void, const void* right_void) {
    const Counter* left = *(Counter **)left_void;
    const Counter* right = *(Counter **)right_void;
    int comparison = right->frequency - left->frequency;
    // compare the word as a tie break for frequency
    return comparison != 0 ? comparison : strcmp(left->word, right->word);
}

void report(Node* root) {
    Node* node = root->next; // skip the first "dummy" value
    int count = 0;
    int max = 0;
    while (node != NULL) {
        node = node->next;
        count++;
    }
    node = root;
    Counter* counters[count];
    for (int i = 0; i < count; i++) {
        counters[i] = node->this;
        node = node->next;
        Counter* counter = counters[i];
        int length = strlen(counter->word);
        max = length > max ? length : max;
    }
    qsort(counters, count, sizeof(Counter *), descending);
    for (int i = 0; i < count; i++) {
        Counter* counter = counters[i];
        printf("%s:", counter->word);
        int pad_length = max - strlen(counter->word);
        for (int j = 0; j < pad_length; j++) {
            putchar(' ');
        }
        for (int j = 0; j < counter->frequency; j++) {
            putchar('*');
        }
        putchar('\n');
    }
    printf("Total words found: %d\n", count);
}

int main(int argc, char** argv) {
    FILE* file_handle = fopen("module46.txt", "r");
    char buffer[255];
    Node* root = create_counter("");

    while (fscanf(file_handle, "%s", buffer) != EOF) {
        int word_length = strlen(buffer);
        char* word = malloc(sizeof(char) * word_length);
        strncpy(word, buffer, word_length);
        bump(root, word);
    }

    report(root);
    fclose(file_handle);
    return 0;
}