#define PCRE2_CODE_UNIT_WIDTH 8

#include <pcre2.h>
#include <stdbool.h>
#include <stdio.h>
#include <string.h>
#include <sys/ipc.h>
#include <sys/msg.h>

#define MSG_TYPE_FILE_NAME 1
#define MSG_TYPE_CONTENTS 2

// Compile with gcc ./validate_and_save.c -lpcre2-8 -o validate_and_save

// structure for message queue
struct mesg_buffer {
    long mesg_type;
    char mesg_text[4096];
} file_name, contents;

bool is_valid_html_file(char const* text)
{
    pcre2_code* re = NULL;
    PCRE2_SPTR pattern = "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">";
    PCRE2_SPTR subject = text;

    int error_number;
    PCRE2_SIZE error_offset;

    re = pcre2_compile(pattern, PCRE2_ZERO_TERMINATED, 0, &error_number, &error_offset, NULL);

    if (re == NULL) {
        PCRE2_UCHAR buf[256];
        pcre2_get_error_message(error_number, buf, sizeof(buf));
        printf("PCRE2 Failed to compile regex '%s' at offset '%zu'\n", pattern, error_offset);
        exit(1);
    }

    pcre2_match_data* match_data
        = pcre2_match_data_create_from_pattern(re, NULL);
    int rc = pcre2_match(re, subject, strlen(subject), 0, 0, match_data, NULL);
    pcre2_match_data_free(match_data);
    pcre2_code_free(re);

    return rc >= 0;
}

void write_to_file(char const* fname, char const* text)
{
    FILE* out = fopen(fname, "w");
    fwrite(text, 1, strlen(text), out);
    fclose(out);
}

int main()
{
    // gcc receiver.c -o receiver
    // ./receiver
    key_t key = -1;
    int msgid;

    // msgget creates a message queue
    // and returns identifier
    msgid = msgget(key, 0666 | IPC_CREAT);

    // msgrcv to receive message
    msgrcv(msgid, &file_name, sizeof(file_name), MSG_TYPE_FILE_NAME, 0);
    msgrcv(msgid, &contents, sizeof(contents), MSG_TYPE_CONTENTS, 0);

    // display the message
    printf("Recevied file name is: %s \n", file_name.mesg_text);
    printf("Received contents: %s\n", contents.mesg_text);

    if (is_valid_html_file) {
        char* fname = calloc(strlen(file_name.mesg_text) + 5, 1);
        strcpy(fname, file_name.mesg_text);
        strcat(fname, ".html");
        write_to_file(fname, contents.mesg_text);
        free(fname);
    }

    // to destroy the message queue
    msgctl(msgid, IPC_RMID, NULL);

    return 0;
}
