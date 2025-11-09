import customtkinter as ctk
from PIL import Image

class MigrationApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # ---------------------------
        # Branding colors
        # ---------------------------
        self.color_primary = "#4A90E2"
        self.color_muted_teal = "#3BA99C"
        self.color_accent_teal = "#5ED0BD"
        self.color_soft_gray = "#A0A0A0"

        # ---------------------------
        # Window setup
        # ---------------------------
        self.title("S2W Product Migration")
        self.geometry("1100x700")
        self.configure(fg_color="white")

        # ---------------------------
        # Header with logo + title
        # ---------------------------
        header = ctk.CTkFrame(self, height=80, corner_radius=0, fg_color=self.color_primary)
        header.pack(fill="x", side="top")

        # Try to load logo
        try:
            logo_img = Image.open("Assets/logo.png")  # make sure this file exists
            self.logo_ctk = ctk.CTkImage(logo_img, size=(50, 50))
            ctk.CTkLabel(header, image=self.logo_ctk, text="", fg_color=self.color_primary).pack(side="left", padx=15)
        except Exception as e:
            print("Logo not found:", e)

        ctk.CTkLabel(header, text="S2W Product Migration",
                     text_color="white", font=("Segoe UI", 24, "bold")).pack(side="left", padx=10)

        # ---------------------------
        # Tab View
        # ---------------------------
        self.tabs = ctk.CTkTabview(
            self,
            segmented_button_fg_color=self.color_soft_gray,
            segmented_button_selected_color=self.color_muted_teal,
            segmented_button_selected_hover_color=self.color_accent_teal,
            segmented_button_unselected_color=self.color_soft_gray,
            segmented_button_unselected_hover_color=self.color_accent_teal,
            text_color="black",
        )
        self.tabs.pack(fill="both", expand=True, padx=10, pady=10)

        self.tabs._segmented_button.configure(font=("Segoe UI", 14, "bold"), height=45)

        # Tabs
        self.cred_tab = self.tabs.add("🔑 Credentials")
        self.prod_tab = self.tabs.add("📦 Products")
        self.help_tab = self.tabs.add("❓ Help")

        # ---------------------------
        # Fill content
        # ---------------------------
        self.create_credentials_tab()
        self.create_products_tab()
        self.create_help_tab()

    def create_credentials_tab(self):
        # Stretch full width, brand background
        frame = ctk.CTkFrame(self.cred_tab, fg_color=self.color_soft_gray, corner_radius=10)
        frame.pack(fill="both", expand=True, padx=20, pady=20)

        ctk.CTkLabel(frame, text="Enter Shopify & WooCommerce Credentials",
                     font=("Segoe UI", 18, "bold"),
                     text_color="black").grid(row=0, column=0, columnspan=2, pady=20)

        fields = ["Shopify Store URL", "Shopify Access Token",
                  "WooCommerce Store URL", "WooCommerce Consumer Key",
                  "WooCommerce Consumer Secret"]

        self.entries = {}
        for i, label in enumerate(fields, start=1):
            ctk.CTkLabel(frame, text=label, anchor="w", text_color="black",
                         font=("Segoe UI", 13)).grid(row=i, column=0, padx=20, pady=10, sticky="e")
            entry = ctk.CTkEntry(frame, width=400, show="*" if "Token" in label or "Secret" in label else None)
            entry.grid(row=i, column=1, padx=20, pady=10, sticky="w")
            self.entries[label] = entry

        # Buttons
        btn_frame = ctk.CTkFrame(frame, fg_color="transparent")
        btn_frame.grid(row=len(fields)+1, column=0, columnspan=2, pady=30)

        ctk.CTkButton(btn_frame, text="Test Shopify", fg_color=self.color_primary, hover_color=self.color_accent_teal).pack(side="left", padx=15)
        ctk.CTkButton(btn_frame, text="Test WooCommerce", fg_color=self.color_muted_teal, hover_color=self.color_accent_teal).pack(side="left", padx=15)

    def create_products_tab(self):
        frame = ctk.CTkFrame(self.prod_tab, fg_color="white", corner_radius=10)
        frame.pack(fill="both", expand=True, padx=20, pady=20)

        ctk.CTkLabel(frame, text="Products Area",
                     font=("Segoe UI", 18, "bold"), text_color="black").pack(pady=20)

        ctk.CTkButton(frame, text="Fetch Products", fg_color=self.color_primary, hover_color=self.color_accent_teal).pack(pady=10)
        ctk.CTkButton(frame, text="Migrate Products", fg_color=self.color_muted_teal, hover_color=self.color_accent_teal).pack(pady=10)

    def create_help_tab(self):
        frame = ctk.CTkFrame(self.help_tab, fg_color="white", corner_radius=10)
        frame.pack(fill="both", expand=True, padx=20, pady=20)

        help_text = (
            "📘 Instructions\n\n"
            "Step 1: Enter your credentials in the Credentials tab.\n"
            "Step 2: Test connections using the provided buttons.\n"
            "Step 3: Go to Products tab and fetch your Shopify products.\n"
            "Step 4: Review and migrate them to WooCommerce.\n"
        )
        ctk.CTkLabel(frame, text=help_text, font=("Segoe UI", 13),
                     text_color="black", justify="left").pack(padx=20, pady=20, anchor="w")


if __name__ == "__main__":
    app = MigrationApp()
    app.mainloop()
