from supabase import create_client

SUPABASE_URL = "https://ruvzgsekvgjjqdgjiqwq.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InJ1dnpnc2VrdmdqanFkZ2ppcXdxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzU4NTMxMDcsImV4cCI6MjA5MTQyOTEwN30.rLzrmtXQRCJSdHHovn2GC_lkzEDF-0mL-jxOCoW_T1k"

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

def hämta_listan():
    response = supabase.table("Lista").select("item").execute()
    return [row["item"] for row in response.data]

def write_listan(item):
    supabase.table("Lista").insert({"item": item}).execute()

def ta_bort(item):
    supabase.table("Lista").delete().eq("item", item).execute()