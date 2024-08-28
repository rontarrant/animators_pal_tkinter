import tkinter as tk

class StateManager:
	def __init__(self):
		self._state = {}
		self._observers = []

	def set_state(self, key, value):
		self._state[key] = value
		self._notify_observers(key)

	def get_state(self, key):
		return self._state.get(key)

	def attach(self, observer):
		self._observers.append(observer)

	def _notify_observers(self, changed_key):
		for observer in self._observers:
			observer.update(self, changed_key
