class Customer:
	def __init__(self, arrival_time, service_start_time, service_time):
		self.__arrival_time = arrival_time;
		self.__service_start_time = service_start_time;
		self.__service_time = service_time;
		self.__service_end_time = self.__service_start_time + self.__service_time;
		self.__wait = self.__service_start_time + self.__arrival_time;

	@property
	def arrival_time(self):
		return self.__arrival_time;
	@arrival_time.setter
	def arrival_time(self, at):
		self.__arrival_time = at;
	@property
	def service_start_time(self):
		return self.__service_start_time;
	@service_start_time.setter
	def service_start_time(self, sst):
		self.__service_start_time = sst;
	@property
	def service_time(self):
		return self.__service_time;
	@service_time.setter
	def service_time(self, st):
		self.__service_time = st;

	@property
	def service_end_time(self):
		return self.__service_start_time + self.__service_time;
	@property
	def wait(self):
		return self.__wait;

# if __name__ == "__main__":