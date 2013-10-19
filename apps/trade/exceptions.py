__author__ = 'rodrigo'



class TradeRuntimeError(RuntimeError):
  error_description = "Unknow error"

class DuplicateSession(TradeRuntimeError):
  error_description = "Duplicated session"

class InvalidOptCodeError(TradeRuntimeError):
  error_description = "Invalid message opt_code"

class InvalidSessionError(TradeRuntimeError):
  error_description = "Invalid session"

class SessionTimeoutError(TradeRuntimeError):
  error_description = "Session timeout"

class InvalidMessageError(TradeRuntimeError):
  error_description = "Invalid message"

class NotAuthorizedError(TradeRuntimeError):
  error_description = "Not authorized"
