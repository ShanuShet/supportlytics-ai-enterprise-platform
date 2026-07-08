"""
Security and Governance Guardrails for Supportlytics AI.
Provides prompt injection detection, PII sanitization, and permission evaluation.
"""
import re
from typing import Dict, Any, List

PROMPT_INJECTION_PATTERNS = [
    r"ignore\s+(all\s+)?previous\s+instructions",
    r"disregard\s+(all\s+)?prior\s+prompts",
    r"system\s+override",
    r"you\s+are\s+now\s+in\s+developer\s+mode",
    r"drop\s+table",
    r"delete\s+from",
    r"sudo\s+rm\s+-rf",
    r"reveal\s+(system\s+)?prompt",
    r"bypass\s+security",
]

PII_PATTERNS = {
    "ip_address": r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b",
    "email": r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b",
    "ssn": r"\b\d{3}-\d{2}-\d{4}\b",
    "credit_card": r"\b(?:\d[ -]*?){13,16}\b",
    "password_keyword": r"(?i)(password|passwd|secret|api_key|token)\s*[:=]\s*\S+",
}

def evaluate_ticket_security(ticket_title: str, ticket_description: str) -> Dict[str, Any]:
    """
    Evaluates an incoming ticket for security threats, prompt injections, and PII exposure.
    Returns safety status, risk score, and detected anomalies.
    """
    combined_text = f"{ticket_title} {ticket_description}"
    threats_detected = []
    
    # Check for prompt injection
    for pattern in PROMPT_INJECTION_PATTERNS:
        if re.search(pattern, combined_text, re.IGNORECASE):
            threats_detected.append(f"Prompt Injection Attack Pattern Detected: '{pattern}'")
            
    # Check for exposed raw secrets or tokens
    if re.search(PII_PATTERNS["password_keyword"], combined_text):
        threats_detected.append("Potential raw credential/secret leakage in ticket text.")
        
    is_safe = len(threats_detected) == 0
    risk_score = 0.95 if not is_safe else 0.05
    
    # Sanitize text
    sanitized_description = sanitize_pii(ticket_description)
    
    return {
        "is_safe": is_safe,
        "risk_score": risk_score,
        "threats": threats_detected,
        "sanitized_description": sanitized_description,
        "status": "APPROVED" if is_safe else "BLOCKED_SECURITY_VIOLATION"
    }

def sanitize_pii(text: str) -> str:
    """Replaces sensitive patterns in ticket text with redacted placeholders."""
    sanitized = text
    # Mask password key-values
    sanitized = re.sub(PII_PATTERNS["password_keyword"], r"\1: [REDACTED_SECRET]", sanitized)
    # Mask SSNs
    sanitized = re.sub(PII_PATTERNS["ssn"], "[REDACTED_SSN]", sanitized)
    # Mask credit cards
    sanitized = re.sub(PII_PATTERNS["credit_card"], "[REDACTED_CARD]", sanitized)
    return sanitized
