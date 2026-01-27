#!/usr/bin/env python3
"""Quick test to see if auth modules load"""
import sys
sys.path.insert(0, "/Users/loucid/Projects/architype/app")

try:
    from core.auth.auth_utils import get_password_hash, verify_password
    print("✅ Auth utils imported successfully")
    
    # Test hashing
    hashed = get_password_hash("testpassword")
    print(f"✅ Password hashed: {hashed[:20]}...")
    
    # Test verification
    is_valid = verify_password("testpassword", hashed)
    print(f"✅ Password verification: {is_valid}")
    
    from models.user.user import User, UserCreate
    print("✅ User models imported successfully")
    
    print("\n🎉 All imports work! Server should start.")
    
except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc()
