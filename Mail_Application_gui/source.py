import smtplib
import tkinter as tk
from tkinter import messagebox


def send_mail():
    global user_email, recipient_entry, subject_entry, message_text
    try:
        # Entries
        email = user_email.get()
        recipient = recipient_entry.get()
        subject = subject_entry.get()
        message = message_text.get("1.0", tk.END)
        if (
            email == ""
            # or pwd == ""
            or recipient == ""
            or subject == ""
            or message == ""
        ):
            messagebox.showinfo("All fields are required", fg="red")
        else:
            # ==================Sender=========================================
            msg = f"Subject: {subject}\n\n{message}".format(subject, message)
            
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            # Login to the email account
            # Send email
            server.sendmail(email, recipient, msg)
            messagebox.showinfo("Success", "Email sent successfully.")
    except smtplib.SMTPException:
        messagebox.showerror("Error", "Failed to send email.")
        server.quit()


def reset_mail():
    # Clear the input
    user_email.delete(0, tk.END)
    recipient_entry.delete(0, tk.END)
    subject_entry.delete(0, tk.END)
    message_text.delete("1.0", tk.END)
    messagebox.showinfo("Success", "Email reset successfull.")


def mail_window():
    global user_email, recipient_entry, subject_entry, message_text

    # ===============================MAIN===============================
    root = tk.Tk()
    root.title("Mail Application")
    root.geometry("1000x1000")

    root.configure(background="lightgreen")


    content_frame = tk.Frame(root, bg="lightgreen")
    content_frame.pack(pady=40)


    user_email_label = tk.Label(
        content_frame, text="Email:", font=("Arial", 12), bg="white", fg="black"
    )
    user_email_label.grid(row=0, sticky=tk.W, padx=5, pady=5)
 
    user_email = tk.Entry(content_frame, width=80)
    user_email.grid(row=0, column=1, padx=5, pady=5)


    recipient_label = tk.Label(
        content_frame, text="Recipient:", font=("Arial", 12), bg="white", fg="black"
    )
    recipient_label.grid(row=2, sticky=tk.W, padx=5, pady=5)
   
    recipient_entry = tk.Entry(content_frame, width=80)
    recipient_entry.grid(row=2, column=1, padx=5, pady=5)


    subject_label = tk.Label(
        content_frame, text="Subject:", font=("Arial", 12), bg="white", fg="black"
    )
    subject_label.grid(row=3, sticky=tk.W, padx=5, pady=5)
    
    subject_entry = tk.Entry(content_frame, width=80)
    subject_entry.grid(row=3, column=1, padx=5, pady=5)


    message_label = tk.Label(
        content_frame, text="Body", font=("Arial", 12), bg="white", fg="black"
    )
    message_label.grid(row=4, sticky=tk.W, padx=5, pady=5)

    message_text = tk.Text(content_frame, height=25, width=60)
    message_text.grid(row=4, column=1, padx=5, pady=5)


    send_button = tk.Button(
        content_frame, text="Send", font=("Arial", 12), command=send_mail
    )
    send_button.grid(row=5, column=1, sticky=tk.W, padx=15, pady=5)


    reset_button = tk.Button(
        content_frame, text="Reset", font=("Arial", 12), command=reset_mail
    )
    reset_button.grid(row=5, column=2, sticky=tk.W, padx=1, pady=5)


    root.mainloop()


mail_window()
